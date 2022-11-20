from faker import Faker
import random
import yaml


def get_answer(data):

    # 读取规则表
    with open('/message/app/resource/answer_rule.yaml') as f:
        rule_list = yaml.load(f, Loader=yaml.FullLoader)

    # 优先级排序
    rule_list = sorted(rule_list, key=lambda x: x['priority'])

    # 循环每一个规则
    for rule in rule_list:

        # 提取接收信息对象
        room_id = data['room_id']
        from_id = data['from_id']

        # 匹配群聊
        if room_id != '' and 'match_rooms' in rule:
            if room_id not in rule['match_rooms']:
                continue

        # 匹配个人
        if 'match_privates' in rule:
            if from_id not in rule['match_privates']:
                continue

        # 匹配关键字
        if not all(map(lambda x: x in data['message'], rule['match_both_words'])):
            continue

        answer_text = _get_answer_text(**rule['answer'])
        return {'action': 'answer', 'text': answer_text}

    return {'action': 'nothing'}


def _get_answer_text(key, value):
    type_to_func = {'text': lambda x: x,
                    'code': lambda x: str(eval(x))}
    return type_to_func[key](value)

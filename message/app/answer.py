from faker import Faker
import random
import yaml

answer_type_to_func = {'text': lambda x: x,
                       'code': lambda x: str(eval(x))}

type_to_id = {'room': ['room_id', 'match_rooms'],
              'private': ['from_id', 'match_privates']}


def get_answer(data):

    # 读取规则表
    with open('/message/app/resource/rule.yaml') as f:
        rule_list = yaml.load(f, Loader=yaml.FullLoader)

    match_rule = rule_list['matching_rules']

    # 循环每一个规则
    for rule_info in match_rule:
        rule = rule_info['rule']
        id_name, match_name = type_to_id[rule['type']]

        if data[id_name] not in rule[match_name]:
            continue

        if not all(map(lambda x: x in data['message'], rule['match_both_words'])):
            continue

        answer_info = rule_info['answer']
        answer_type = answer_info['type']
        answer_func = answer_type_to_func[answer_type]
        answer_text = answer_func(answer_info['value'])
        return {'action': 'answer', 'text': answer_text}

    return {'action': 'nothing'}

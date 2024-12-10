def find_common_participants(participants_first_group, participants_second_group, sep=','):

    participants1 = set(participants_first_group.split(sep))
    participants2 = set(participants_second_group.split(sep))
    common_participants = participants1.intersection(participants2)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)

print(common_participants)

# -*- coding: utf-8 -*-

# points variable
win_point = 3
draw_point = 1


def url_to_id(link, model):
    """
    :param link: string, shortcut for django model
    :param model: django model
    :return: django model where shortcut = link
    """
    try:
        return model.objects.get(shortcut=link)
    except model.DoesNotExist:
        return None


def add_points_to_team(team, goals_scored, goals_conceded):
    """
    :param team: team_stat model object
    :param goals_scored: integer, goals that team scored
    :param goals_conceded: integer, goals that team conceded
    :return: None
    """
    team.match_count += 1
    team.goals_scored += goals_scored
    team.goals_conceded += goals_conceded
    if goals_scored > goals_conceded:
        team.wins += win_point
        team.points += 3
    elif goals_scored < goals_conceded:
        team.loses += 1
    else:
        team.draws += draw_point
        team.points += 1
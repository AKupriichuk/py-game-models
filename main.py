import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", 'r') as f:
        players_data = json.loads(f.read())

    for player_info in players_data:
        race_data = player_info.get('race')
        race_obj = None
        if race_data:
            race_obj, _ = Race.objects.get_or_create(
                name=race_data['name'],
                defaults={"description": race_data.get('description', '')},
            )

        guild_data = player_info.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data['name'],
                defaults={"description": guild_data.get('description')},
            )

        Player.objects.get_or_create(
            nickname=player_info['nickname'],
            defaults={
                "email": player_info['email'],
                "bio": player_info['bio'],
                "race": race_obj,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()

from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    result = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    today = date.today()
    yesterday = today - timedelta(days=1)
    b_yesterday = today - timedelta(days=2)
    week = timedelta(days=7)

    if not users:
        return {}
    else:
        for person in users:
            person["birthday"] = person["birthday"].replace(year=today.year)
            birthday = person["birthday"].strftime('%A')
            if today.strftime('%A') == "Monday":
                if person['birthday'] == yesterday or person["birthday"] == b_yesterday:
                    result["Monday"].append(person["name"].split()[0])
                    continue
            if today <= person["birthday"] <= today + week:
                if birthday == "Saturday" or birthday == "Sunday":
                    result["Monday"].append(person["name"].split()[0])
                else:
                    result[birthday].append(person["name"].split()[0])
            # if new year
            else:
                if (today + week).year == today.year + 1:
                    person["birthday"] = person["birthday"].replace(year=today.year + 1)
                    new_year_birthday = person["birthday"].strftime('%A')
                    if today <= person["birthday"] <= today + week:
                        if new_year_birthday == "Saturday" or new_year_birthday == "Sunday":
                            result["Monday"].append(person["name"].split()[0])
                        else:
                            result[new_year_birthday].append(person["name"].split()[0])
                continue

    clear_result = {key: value for key, value in result.items() if value}
    return clear_result


if __name__ == "__main__":
    users = [
        {"name": "Jan Week", "birthday": datetime(1976, 1, 17).date()},
        {"name": "Luck St", "birthday": datetime(1976, 1, 20).date()},
        {"name": "Matt St", "birthday": datetime(1978, 1, 21).date()},
        {"name": "Ken Do", "birthday": datetime(1976, 1, 19).date()},
        {"name": "Nick", "birthday": datetime(1966, 1, 22).date()},
        {"name": "John Doe", "birthday": datetime(1979, 1, 24).date()},
        {"name": "Elle Harper", "birthday": datetime(1976, 12, 26).date()},
        {"name": "Leo B", "birthday": datetime(1986, 12, 28).date()},
        {"name": "Kerry", "birthday": datetime(1998, 1, 2).date()},
        {"name": "Lu Ken", "birthday": datetime(1966, 1, 1).date()},
        {"name": "Marry", "birthday": datetime(1969, 12, 31).date()},
        {"name": "Tommy", "birthday": datetime(1999, 1, 3).date()},
    ]
    result = get_birthdays_per_week(users)
    # Виводимо результат
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

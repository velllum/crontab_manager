import csv

from app import db
from app import models as ms


def check_data(dct):
    if dct.get("slug") == "":
        dct["slug"] = None
    if dct.get("inn") == "":
        dct["inn"] = None
    if dct.get("subject_id") == "":
        dct["subject_id"] = None
    if dct.get("type_id") == "":
        dct["type_id"] = None
    if dct.get("name") == "":
        dct["name"] = None
    return dct


def set_organization():

    cv = open("accounts_organization_slug_linux.csv")
    dict_reade = csv.DictReader(cv)

    update = 0
    create = 0
    enum = 0

    for reade in dict_reade:

        dct = check_data(dict(reade))

        enum += 1

        queryset = db.session.query(ms.Organizations).filter_by(id=dct.get("id"))

        if queryset.first():
            print(f"update {dct}")
            queryset.update(dct)
            db.session.commit()
            update += 1
        else:
            dct.pop("id")
            print(f"create {dct}")
            org = ms.Organizations(**dct)
            db.session.add(org)
            db.session.commit()
            create += 1

    print(f"update {update}")
    print(f"update {create}")
    print(f"update and create {create + update}")

    print(f"enumerate {enum}")


if __name__ == "__main__":
    set_organization()

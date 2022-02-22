import csv

from app import db
from app import models as ms


def set_organization():

    cv = open("accounts_organization_slug_linux.csv")
    read = csv.DictReader(cv)

    update = 0
    create = 0
    enum = 0

    for r in read:

        r = dict(r)

        enum += 1

        queryset = db.session.query(ms.Organizations).filter_by(id=r.get("id"))

        if queryset.first():
            print(f"update {r}")
            queryset.name = r.get("name")
            db.session.commit()
            update += 1
        else:
            print(f"create {r}")
            org = ms.Organizations(**r)
            db.session.add(org)
            db.session.commit()
            create += 1

    print(f"update {update}")
    print(f"update {create}")
    print(f"update and create {create + update}")

    print(f"enumerate {enum}")


if __name__ == "__main__":
    set_organization()

from app import db
from app import models as ms


def set_file_group_user():

    file_id = [1, 3]

    for user in db.session.query(ms.MyUser).all():

        print(f"<{user.lastname} {user.username} {user.patronymic}> <{user.email}>")

        user_files = db.session.query(ms.FileGroupUser).filter_by(myuser_id=user.id).all()

        name_files = [get_name(f.filegroup_id) for f in user_files]
        print(name_files)

        if not user_files:
            for _id in file_id:
                f = ms.FileGroupUser
                f.myuser_id = user.id
                f.filegroup_id = _id
                # db.session.add(f)
                # db.session.commit()
                print("общий доступ и КУО", get_name(f.filegroup_id))
            continue

        if "общий доступ" not in name_files:
            f = ms.FileGroupUser
            f.myuser_id = user.id
            f.filegroup_id = file_id[0]
            # db.session.add(f)
            # db.session.commit()
            print("общий доступ", f)

        if "КУО" not in name_files:
            f = ms.FileGroupUser
            f.myuser_id = user.id
            f.filegroup_id = file_id[1]
            # db.session.add(f)
            # db.session.commit()
            print("КУО", f)

        # break


def get_name(_id):

    query = db.session.query(ms.FileGroup).get(_id)

    if query:
        return query.name


set_file_group_user()

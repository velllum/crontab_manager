from app import db
from app import models as ms


def set_file_group_user():

    file_group_id = [1, 3]

    for user in db.session.query(ms.MyUser).all():


        lst_obj_my_user = db.session.query(ms.FileGroupUser).filter_by(myuser_id=user.id).all()

        print(lst_obj_my_user[0].filegroup_id.name)

        lst_my_user_name = [f.filegroup_id for f in lst_obj_my_user]
        print(lst_my_user_name)

        if not lst_obj_my_user.name:
            for y_id in file_group_id:
                fu = ms.FileGroupUser
                fu.myuser_id = user.id
                fu.filegroup_id = y_id
                # db.session.add(fu)
                # db.session.commit()
                print("общий доступ и КУО", fu)
            continue

        if "общий доступ" not in lst_my_user_name:
            fu = ms.FileGroupUser
            fu.myuser_id = user.id
            fu.filegroup_id = file_group_id[0]
            # db.session.add(fu)
            # db.session.commit()
            print("общий доступ", fu)

        if "КУО" not in lst_my_user_name:
            fu = ms.FileGroupUser
            fu.myuser_id = user.id
            fu.filegroup_id = file_group_id[1]
            # db.session.add(fu)
            # db.session.commit()
            print("КУО", fu)

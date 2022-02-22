import datetime

from app import models as ml
from app import db


def set_ticket_status():
    """- установить статус заявки, в фоновом режиме"""

    ID_STATUS_CLOSE = 13
    ID_STATUS_FINISH = 12

    # берем объект, со статусом закрыто, по id 13
    status_close = db.session.query(ml.Status).get(ID_STATUS_CLOSE)

    # получить список тикетов со статусом выполнено, по id 12
    status_finish = db.session.query(ml.Ticket).filter_by(status_id=ID_STATUS_FINISH).all()
    # filter(models.ticket().finished_at.between('2021-05-17', '2022-01-17')).all()
    # filter(User.birthday.between('1985-01-17', '1988-01-17'))
    # filter(DateClass.date_in >= d1).filter(DateClass.date_in <= d2)

    len_status_finish = len(status_finish)

    # получить текущую дату
    # today = datetime.datetime.now(datetime.timezone.utc)
    today = datetime.datetime.now()

    for e, ticket in enumerate(status_finish, 1):

        # проверяем дату выполнения на существование,
        # если она None делаем пропуск в цикле
        if not ticket.finished_at:
            print("=" * 50)
            print(f"[Новая заявка], {e}), "
                  f"общее кол.: {len_status_finish}, "
                  f"id заявки: {ticket.id}, имя: {ticket.status.name}, "
                  f"описание: {ticket.title}, текущая дата: {today}, "
                  f"дата выполнения: {ticket.finished_at}, "
                  f"кол. отведенных дней до статуса закрыть: {ticket.agreement.working_days_count}"
                  )
            continue

        # получить разницу в датах
        days_delta = today - ticket.finished_at.replace(tzinfo=None)

        # проверяем существование числа дней для перевода статуса в закрытые,
        # если она None делаем пропуск в цикле
        if not ticket.agreement.working_days_count:
            print("=" * 50)
            print(f"[В базе не указанно кол. дней на закрытие, после выполнения], {e}), "
                  f"общее кол.: {len_status_finish}, "
                  f"id заявки: {ticket.id}, имя: {ticket.status.name}, "
                  f"описание: {ticket.title}, текущая дата: {today}, "
                  f"дата выполнения: {ticket.finished_at}, "
                  f"кол. дней после статуса выполнено: {days_delta}, "
                  f"кол. отведенных дней до статуса закрыть: {ticket.agreement.working_days_count}"
                  )
            continue

        # если полученная дата больше даты установленной для ее закрытия,
        # то заявку переводим в статус закрытые
        if days_delta.days >= ticket.agreement.working_days_count:
            print("=" * 50)
            print(f"[Закрыта], {e}), "
                  f"общее кол.: {len_status_finish}, "
                  f"id заявки: {ticket.id}, имя: {ticket.status.name}, "
                  f"описание: {ticket.title}, текущая дата: {today}, "
                  f"дата выполнения: {ticket.finished_at}, "
                  f"кол. дней после статуса выполнено: {days_delta}, "
                  f"кол. отведенных дней до статуса закрыть: {ticket.agreement.working_days_count}"
                  )
            ticket.status_id = status_close.id
            # db.session.commit()

        else:
            # если не одна проверка не пройдена то записываем в файл log.txt информацию в виде ошибки,
            print("= " * 25)
            print(f"[Срок не пришёл], {e}), "
                  f"общее кол.: {len_status_finish}, "
                  f"id заявки: {ticket.id}, имя: {ticket.status.name}, "
                  f"описание: {ticket.title}, текущая дата: {today}, "
                  f"дата выполнения: {ticket.finished_at}, "
                  f"кол. дней после статуса выполнено: {days_delta}, "
                  f"кол. отведенных дней до статуса закрыть: {ticket.agreement.working_days_count}"
                  )
            print("= " * 25)

    print("*" * 25, today, "*" * 25)

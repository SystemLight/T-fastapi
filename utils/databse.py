from functools import wraps

from sqlalchemy.orm import Session

from . import http


def transition(func):
    """

    当一个事务调用另外一个事务时，可能需要禁用子事务那么可以传入_dt=True来禁用方法的事务

    :param func:
    :return:

    """

    @wraps(func)
    def wrap(db: Session, *args, **kwargs):
        dt = kwargs.get("_dt", False)

        if kwargs.get("_dt", None) is not None:
            del kwargs["_dt"]

        # 禁用事务
        if dt:
            return func(db, *args, **kwargs)

        try:
            result = func(db, *args, **kwargs)
        except Exception as e:
            db.rollback()
            raise http.FailException(message=str(e))
        else:
            db.commit()
        return result

    return wrap

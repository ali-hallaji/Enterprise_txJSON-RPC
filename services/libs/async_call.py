import time
import datetime

from functools import wraps
from twisted.internet import reactor
from twisted.internet.threads import deferToThreadPool
from txjsonrpc.web.jsonrpc import with_activity_log

from base_handler import exception_handler
from core import toLog
from core.threading_pool.core_thread import get_twisted_pool as pool
from config.settings import CORE_NAME
from config.settings import DEBUG


def asynchronous(cls):

    cls = exception_handler(cls)
    with_activity_log(cls)

    @wraps(cls)
    def async(*args, **kwargs):
        """
           This asynchronous call function.
        """

        args = list(args)
        username = args.pop(1)
        address = args.pop(1)
        args = tuple(args)

        # start time
        ts = time.time()
        start_time = datetime.datetime.now().strftime('%H:%M:%S')

        # Pass to defer
        worker = deferToThreadPool(reactor, pool(), cls, *args, **kwargs)
        # worker = deferToThread(cls, *args, **kwargs)

        # Handle defer
        worker.addCallback(timeit, username, address, start_time, ts, *args)
        worker.addErrback(to_log_error)

        return worker

    return async


def timeit(result, username, address, start_time, ts, *args):

    if DEBUG:
        # End of time execute work
        func_name = args[0].__class__.__full_name__
        te = time.time()

        msg = "start from: {0} >|< username: {1}  -|- "
        msg += "time: {2:2.4f} sec -|- func: {3} -- address: {4} -- args: {5}"
        msg = msg.format(
            start_time,
            username,
            te - ts,
            func_name,
            address,
            args[1:]
        )
        toLog(msg, 'request')

        # set_activity_log(username, address, func_name, args[1:])

    return result


def to_log_error(failure):
    toLog(str(failure), 'error')



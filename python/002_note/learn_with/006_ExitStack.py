import contextlib
import sys
from typing import IO
from typing import Optional


# 使用with
def output_line_v1(s: str, stream: IO[str], *, filename: Optional[str] = None, ) -> None:
    if filename is not None:
        with open(filename, 'w') as f:
            for output_stream in (f, stream):
                output_stream.write(f'{s}\n')
    else:
        stream.write(f'{s}\n')


# 使用contextlib
def output_line_v2(s: str, stream: IO[str], *, filename: Optional[str] = None, ) -> None:
    if filename is not None:
        f = open(filename, 'w')
        streams = [stream, f]
        ctx = f
    else:
        streams = [stream]
        ctx = contextlib.nullcontext()
    with ctx:
        for output_stream in streams:
            output_stream.write(f'{s}\n')


# 使用ExitStack()
def output_line_v3(s: str, stream: IO[str], *, filename: Optional[str] = None, ) -> None:
    with contextlib.ExitStack() as ctx:
        streams = [stream]
        if filename is not None:
            streams.append(ctx.enter_context(open(filename, 'w')))

        for output_stream in streams:
            output_stream.write(f'{s}\n')


# output_line_v1('hello world', stream=sys.stdout)
# output_line_v1('googlebye world', stream=sys.stdout, filename='log.log')

# output_line_v2('hello world', stream=sys.stdout)
# output_line_v2('googlebye world', stream=sys.stdout, filename='log.log')

output_line_v3('hello world', stream=sys.stdout)
output_line_v3('googlebye world', stream=sys.stdout, filename='log.log')

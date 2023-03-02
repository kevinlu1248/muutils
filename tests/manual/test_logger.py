# NOTE: This is a manual test. The tests in this file are not run by pytest.
from muutils.logger import Logger

logger = Logger()


logger.log("hello")

logger["test_stream"]("hello test stream")

logger.mystream("hello mystream")
logger.mystream("hello mystream, again")

logger.log("something is wrong!", -10)
logger.log("something is very wrong!", -30)

logger.log("not very important", 50)

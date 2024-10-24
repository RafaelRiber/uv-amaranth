# Temporary (?) way of calling pytest with uv
# Maybe use the uv cache in the CI to avoid this ?
import pytest
retcode = pytest.main()

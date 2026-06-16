import pytest
from pytest import CaptureFixture

from app.main import main


class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys: CaptureFixture[str]) -> None:
        self.capsys = capsys

    def test_main(self) -> None:
        main()
        captured = self.capsys.readouterr()
        assert captured.out == "Hello World\n20\n"

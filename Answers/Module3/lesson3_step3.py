import pytest

from Answers.Module1.lesson6_step10 import insert_required_data


class TestInsert:
    def test_insert_data_to_required_fields_only1(self, browser):
        link = "http://suninjuly.github.io/registration1.html"
        result = insert_required_data(browser, link)
        assert result is None

    @pytest.mark.xfail
    def test_insert_data_to_required_fields_only2(self, browser):
        link = "http://suninjuly.github.io/registration2.html"
        result = insert_required_data(browser, link)
        assert result is None


if __name__ == "__main__":
    pytest.main()

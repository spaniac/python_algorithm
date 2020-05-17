import unittest
from pprint import pprint
from unittest.mock import patch

from python_fundamentals.momo import request_all_users


class MockingTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # def test_mocking_example(self):
    #     mock = Mock(return_value='Hello, Mock!')
    #     print(mock())
    #     mock.return_value = 'Hello, world!'
    #     print(mock())
    #
    #     mock1 = Mock(side_effect=Exception('Oppa!'))
    #     # mock1()
    #
    #     mock2 = Mock(side_effect=[1, 2, 3, 4, 5])
    #     for _ in range(5):
    #         print(mock2())
    #     mock2.side_effect = [3, 2, 1, 5, 4]
    #     for _ in range(5):
    #         print(mock2())
    #
    #     mock3 = Mock()
    #     mock3.return_value = "안녕하세요~"
    #     mock3.attr1 = '박세준'
    #     mock3.attr2 = 'set_attr'
    #     print(mock3.attr1)
    #     print(mock3.attr2)
    #     print(mock3())
    #     mock3.assert_called()
    #
    #     mock4 = Mock()
    #     # 한 번이라도 호출이 안되었는지를 검증
    #     mock4.assert_not_called()
    #     mock4()
    #     # mock4.assert_not_called()
    #
    #     # 한 번이라도 호출이 되었는지를 검증
    #     mock4.assert_called()
    #     # 한 번만 호출이 되었는지를 검증
    #     mock4.assert_called_once()
    #     mock4()
    #     # mock4.assert_called_once()
    #     mock4(1, 3, pk=2)
    #     print(mock4.call_args)
    #
    # def test_magic_mock_example(self):
    #     # mock = Mock()
    #     # mock.__str__.return_value
    #     # mock.__str__ = Mock(return_value="I'm a mock")
    #     mock = MagicMock()
    #     print(mock.__str__.return_value)
    #     mock.__str__.return_value = "I'm a magic mock."
    #     print(str(mock))

    """
    patch 데코레이터는 context manager다.
    함수 또는 클래스 내부에서 호출하는 특정 attribute를 새로운 MagicMock로 대체한다.
    (원문)
    `patch` acts as a function decorator, class decorator or a context
    manager. Inside the body of the function or with statement, the `target`
    is patched with a `new` object. When the function/with statement exits
    the patch is undone.
    
    그래서 patch의 mocking 경로를 잡아줄 때는 patching하려는 attribute의 선언 경로가
    아닌 호출 경로를 명시해야 한다.
    """

    @patch("python_fundamentals.momo.request_get_user_list", return_value={
        "count": 50,
        "next": "http://127.0.0.1:8000/blog?page=2",
        "previous": None,
        "results": [
            {
                "id": 1,
                "created_at": "2020-05-15T10:22:53.157479Z",
                "updated_at": "2020-05-15T10:22:53.157479Z",
                "is_deleted": False,
                "deleted_at": None,
                "email": "vvargas@rivera-diaz.com",
                "password": "!W6O6cbOvT",
                "nickname": "Laura Owens",
                "last_login": None
            }, ]})
    def test_get_user_list(self, mock_result):
        exp_result = {
            "count": 50,
            "next": "http://127.0.0.1:8000/blog?page=2",
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "created_at": "2020-05-15T10:22:53.157479Z",
                    "updated_at": "2020-05-15T10:22:53.157479Z",
                    "is_deleted": False,
                    "deleted_at": None,
                    "email": "vvargas@rivera-diaz.com",
                    "password": "!W6O6cbOvT",
                    "nickname": "Laura Owens",
                    "last_login": None
                }, ]}
        as_result = request_all_users()
        self.assertEqual(exp_result, as_result)
        pprint(mock_result.return_value)

    # @patch("requests.get")
    # def test_get_user_list2(self, mock_result):
    #     response = mock_result.return_value
    #     response.status_code = 200
    #     response.json.return_value = {
    #         "count": 50,
    #         "next": "http://127.0.0.1:8000/blog?page=2",
    #         "previous": None,
    #         "results": [
    #             {
    #                 "id": 1,
    #                 "created_at": "2020-05-15T10:22:53.157479Z",
    #                 "updated_at": "2020-05-15T10:22:53.157479Z",
    #                 "is_deleted": False,
    #                 "deleted_at": None,
    #                 "email": "vvargas@rivera-diaz.com",
    #                 "password": "!W6O6cbOvT",
    #                 "nickname": "Laura Owens",
    #                 "last_login": None
    #             }, ]}
    #
    #     as_result = request_get_user_list()
    #
    #     exp_result = {
    #         "count": 50,
    #         "next": "http://127.0.0.1:8000/blog?page=2",
    #         "previous": None,
    #         "results": [
    #             {
    #                 "id": 1,
    #                 "created_at": "2020-05-15T10:22:53.157479Z",
    #                 "updated_at": "2020-05-15T10:22:53.157479Z",
    #                 "is_deleted": False,
    #                 "deleted_at": None,
    #                 "email": "vvargas@rivera-diaz.com",
    #                 "password": "!W6O6cbOvT",
    #                 "nickname": "Laura Owens",
    #                 "last_login": None
    #             }, ]}
    #     self.assertEqual(exp_result, as_result)
    #     pprint(exp_result)
    #     pprint(as_result)

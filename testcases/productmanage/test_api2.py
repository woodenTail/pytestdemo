import allure

@allure.epic("项目名称：木鸢自动化测试项目")
@allure.feature("模块名称：商品管理模块")
class TestApi2:

    @allure.story("接口名称：测试星瑶")
    def test_xingyao(self):
        print("测试3")

    @allure.story("接口名称：test_微微")
    def test_product_manage_weiwei(self):
        print("测试4")
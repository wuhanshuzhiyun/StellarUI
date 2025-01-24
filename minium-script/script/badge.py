from utils import push_log

from minium import WXMinium, Page, MiniTest

PATH_NAME = "/mp/badge-demo/badge-demo"

LOG_FILE = f"{__name__.split(".")[-1]}.txt"

STYLES = [
	{"width": 14, "height": 14, "background-color": "rgb(238, 10, 36)", "text": "1"},
	{"height": 14, "background-color": "rgb(238, 10, 36)", "text": "99+"},
	{"height": 14, "background-color": "rgb(238, 10, 36)", "text": "HOT"},
	{"width": 6, "height": 6, "background-color": "rgb(238, 10, 36)"},
	{"width": 6, "height": 6, "background-color": "rgb(19, 183, 22)"},
	{"width": 14, "height": 14, "background-color": "rgb(19, 183, 22)", "text": "1"},
	{"height": 14, "background-image": "linear-gradient(to right, rgb(66, 83, 216), rgb(213, 51, 186))",
	 "text": "99+"},
	{"height": 14, "background-image": 'url("https://image.whzb.com/chain/StellarUI/image/fire.png")',
	 "text": "true"},
]


class BadgeTest(MiniTest):
	mini: WXMinium
	_page: Page


	def _to_page(self):
		self._page = self.mini.app.navigate_to(PATH_NAME)
		self._page.wait_for(1)

	def _test_path(self):
		title = self._page.get_element("view.title-center")
		self.assertEqual(title.text, "徽标", "页面标题不正确")
		components = self._page.get_elements("view.ste-badge-root .ste-badge-content")
		self.assertEqual(len(components), 21, "组件数量不正确")
		for i in range(len(STYLES)):
			push_log(f"component-{i + 1}:start", LOG_FILE)
			style = STYLES[i]
			component = components[i]
			if style.get("width"):
				self.assertEqual(component.styles("width")[0], str(style.get("width")) + "px", "组件样式width不正确")
			if style.get("height"):
				self.assertEqual(component.styles("height")[0], str(style.get("height")) + "px", "组件样式height不正确")
			if style.get("text"):
				self.assertEqual(component.text, style.get("text"), "组件内容不正确")
			if style.get("background-color"):
				self.assertEqual(component.styles("background-color")[
					0], style.get("background-color"), "组件样式background-color不正确")
			if style.get("background-image"):
				self.assertEqual(component.styles("background-image")[
					0], style.get("background-image"), "组件样式background-image不正确")
			push_log(f"component-{i + 1}:success", LOG_FILE)


	def run_test(self, mini: WXMinium):
		self.mini = mini
		try:
			push_log("test start", LOG_FILE)
			push_log(f"to path: {PATH_NAME}", LOG_FILE)
			self._to_page()
			self._test_path()
			push_log("test success", LOG_FILE)
		except Exception as e:
			# 记录错误到outputs
			push_log(str(e), LOG_FILE)
		self._page.wait_for(1)
		self._page.app.navigate_back()
		self._page.wait_for(1)

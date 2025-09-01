from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.clock import Clock

# تحميل ملف التصميم
Builder.load_file("design.kv")

class SplashScreen(Screen):
    def on_enter(self):
        # الانتقال بعد 3 ثوانٍ للشاشة الرئيسية
        Clock.schedule_once(self.go_to_main, 3)

    def go_to_main(self, dt):
        self.manager.transition.direction = "left"
        self.manager.current = "main"

class MainScreen(Screen):
    def calculate(self):
        """حساب الاستهلاك"""
        try:
            prev = float(self.ids.prev_input.text or 0)
            curr = float(self.ids.curr_input.text or 0)
            consumption = curr - prev
            if consumption < 0:
                self.ids.result_label.text = "❌ القراءة الحالية أقل من السابقة"
            else:
                total_cost = consumption * 0.1
                self.ids.result_label.text = f"الاستهلاك: {consumption:.2f} وحدة\nالتكلفة: {total_cost:.2f} دينار"
        except ValueError:
            self.ids.result_label.text = "⚠️ يرجى إدخال أرقام صحيحة"

class ElectricityApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(MainScreen(name="main"))
        return sm

if __name__ == "__main__":
    ElectricityApp().run()
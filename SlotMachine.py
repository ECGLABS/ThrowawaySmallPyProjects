import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SlotMachine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎰 Slot Machine")
        self.setFixedSize(400, 300)

        self.reel_symbols = ["🍒", "🔔", "🍋", "🍉", "⭐", "7️⃣"]
        self.initUI()

    def initUI(self):
        # Labels for slot reels
        self.reel_labels = [QLabel("❓") for _ in range(3)]
        for label in self.reel_labels:
            label.setFont(QFont("Arial", 48))
            label.setAlignment(Qt.AlignCenter)

        # Spin button
        self.spin_button = QPushButton("Spin 🎲")
        self.spin_button.setFont(QFont("Arial", 18))
        self.spin_button.clicked.connect(self.spin_reels)

        # Layouts
        reel_layout = QHBoxLayout()
        for label in self.reel_labels:
            reel_layout.addWidget(label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(reel_layout)
        main_layout.addWidget(self.spin_button)

        self.setLayout(main_layout)

    def spin_reels(self):
        results = [random.choice(self.reel_symbols) for _ in range(3)]
        for label, symbol in zip(self.reel_labels, results):
            label.setText(symbol)

        if results.count(results[0]) == 3:
            QMessageBox.information(self, "🎉 Jackpot!", "You WIN! 🎉")
        else:
            QMessageBox.information(self, "Try Again", "Not a match, spin again!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SlotMachine()
    window.show()
    sys.exit(app.exec_())

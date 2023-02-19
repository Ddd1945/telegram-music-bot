import sqlite3


class BotDataBase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def toggle_on(self, user_id):
        result = self.cursor.execute('UPDATE `users` SET `is_playing` = ? WHERE `user_id` = ?', (1, user_id,))
        return self.conn.commit()

    def toggle_off(self, user_id):
        result = self.cursor.execute('UPDATE `users` SET `is_playing` = ? WHERE `user_id` = ?', (0, user_id,))
        return self.conn.commit()

    def is_playing(self, user_id):
        result = self.cursor.execute('SELECT `is_playing` FROM `users` WHERE `user_id` = ?', (user_id,))
        return result.fetchone()[0]

    def user_exists(self, user_id):
        result = self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id` = ?', (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id):
        result = self.cursor.execute('INSERT INTO `users` (`user_id`) VALUES(?)', (user_id,))
        return self.conn.commit()

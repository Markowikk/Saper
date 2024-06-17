class ScoreBoard:

    def write_to_score_board_file(self, filename, end_time, start_time, nickname):
        """
                Write the player's score to the scoreboard file.
                The score is calculated as the elapsed time between start and end times.
                Each entry in the file contains the player's nickname and their score in points.

                :param filename: Name of the file to write the score to
                :param end_time: The time when the game ended
                :param start_time: The time when the game started
                :param nickname: The player's nickname
                :return: None
                """
        elapsed_time = end_time - start_time
        with open(filename, 'a') as file:
            file.write(nickname + " - " + str(elapsed_time) + " points")

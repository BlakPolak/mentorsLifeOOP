import csv
import random
import time
import os
from person import Person


class Mentor(Person):
    """
    This class represents real mentor in Codecool

        Args:
            nickname: stores mentor nickname
            energy_level: stores mentor energy
            humanity_level: describes how far is mentor from becoming human

    """
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, energy_level, humanity_level):
        """
        Initialize object args
            Args:
                nickname: stores mentor nickname
                energy_level: stores mentor energy
                humanity_level: describes how far is mentor from becoming human
            Returns:
            None
        """
        Person.__init__(self, first_name, last_name, year_of_birth, gender)
        self.nickname = Person.check_if_correct(nickname, str)
        self.energy_level = Person.check_if_correct(energy_level, str)
        self.humanity_level = Person.check_if_correct(humanity_level, str)

    def __str__(self):
        return self.first_name+" "+self.last_name

    @staticmethod
    def create_by_csv(filename="data/mentors.csv"):
        """
        Loads mentors data from csv file.

        Args:
            filename: file path for csv file

        Returns:
            List of Mentor objects
        """
        list_of_mentors_object = []
        with open(filename) as file:
            file_reader = csv.reader(file)
            for data in file_reader:
                list_of_mentors_object.append(Mentor(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        return list_of_mentors_object

    def is_loving_gymnastic(self, mood_for_gymnastic):
        """
        Checks if particular student is happy doing gymnastics

        Args:
            mood_for_gymnastic: describes level of student mood for gymnastic.

        Returns:
            True: if student enjoys gymnastics
            False: if student doesnt enjoy gymnastics
        """
        if random.randint(0, 10) < mood_for_gymnastic:
            return False
        return True

    def is_paying_attention(self, knowledge_desire):
        """
        Checks if particular student pay attention doing during speech

        Args:
            knowledge_desire: describes level of student knowledge desire.

        Returns:
            True: if student pays attention
            False: if student doesnt pay attention
        """
        if random.randint(0, 10) < knowledge_desire:
            return False
        return True

    def do_gymnastics(self, students):
        """
        Executes mentor's gymnastic program in order to increase students energy.

        Args:
            students: list of Students objects

        Returns:
            None
        """
        print("\n\033[1mMentor "+self.first_name+" is starting proper gymnastics routine...\033[0m\n")
        time.sleep(2)
        for student in students:
            if student.first_name[-1] == 'a':
                his_or_her = 'Her'
            else:
                his_or_her = 'His'
            if self.is_loving_gymnastic(student.mood_for_gymnastic):
                student.energy_level += 2
                self.humanity_level += 1
                print("\x1b[32mStudent "+student.first_name, student.last_name + " enjoyed gymnastics and  gains some energy.\x1b[0m\n"+
                      str(his_or_her) + " actual energy level is", student.energy_level)
                print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now\n")
                time.sleep(2)
            else:
                student.energy_level -= 2
                self.humanity_level -= 1
                print("\x1b[31mStudent " + student.first_name, student.last_name
                      + " hates gymnastics and loose some energy.\x1b[0m\n"+
                      str(his_or_her) + " actual energy level is", student.energy_level)
                print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now\n")
                time.sleep(2)
        time.sleep(2)
        os.system('clear')

    def give_motivational_speech(self, students):
        """
        Executes mentor's motivational speech program in order to increase students knowledge.

        Args:
            students: list of Students objects

        Returns:
            None
        """
        print("\n\033[1mMentor " + self.first_name + " gives great motivational speech ...\033[0m\n")
        time.sleep(2)
        for student in students:
            if student.first_name[-1] == 'a':
                his_or_her = 'Her'
            else:
                his_or_her = 'His'
            if self.is_paying_attention(student.knowledge_desire):
                student.knowledge_level += 2
                self.humanity_level += 1
                print("\x1b[32mStudent " + student.first_name, student.last_name +
                      " was paying attention and gains some knowledge.\x1b[0m\n" +
                      str(his_or_her) + " actual knowledge level is", student.knowledge_level)
                print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now\n")
            else:
                student.energy_level -= 2
                self.humanity_level -= 1
                print("\x1b[31mStudent " + student.first_name, student.last_name +
                      " wasn't paying attention and just loose some energy.\x1b[0m\n" +
                      str(his_or_her) + " actual energy level is", student.energy_level)
                print(self.first_name, self.last_name + " has " + str(self.humanity_level) + " humanity points now\n")
            time.sleep(2)
        os.system('clear')

    def give_private_mentoring(self, student):
        """
        Executes mentor's private mentoring program in order to increase student knowledge.

        Args:
            student: Student object

        Returns:
            None
        """
        print("\n\033[1mMentor " + self.first_name + " gives private mentoring for",
              student.first_name, student.last_name + "\033[0m\n")
        time.sleep(2)
        self.humanity_level += 1
        student.knowledge_level += 2
        print("\x1b[32mMentors humanity has increased.\x1b[0m\n" + self.first_name,
              self.last_name + " has " + str(self.humanity_level) + " humanity points now.")
        time.sleep(0.5)
        print("\x1b[32mStudent " + student.first_name, student.last_name + " begins to understand a lot more!\x1b[0m\n" +
              "Actual knowledge level is", student.knowledge_level, "\n")
        time.sleep(2)

    def drink_coffee_with_student(self, student):
        """
        Executes mentor's drink coffee program in order to increase student energy.

        Args:
            student: Student object

        Returns:
            None
        """
        print("\n\033[1mMentor " + self.first_name + " drinks coffee with ",
              student.first_name, student.last_name + "\033[0m\n")
        time.sleep(2)
        self.humanity_level += 1
        student.energy_level += 2
        print("\x1b[32mMentors humanity has increased.\x1b[0m\n"+ self.first_name,
              self.last_name + " has " + str(self.humanity_level) + " humanity points now")
        time.sleep(0.5)
        print("\x1b[32mStudent " + student.first_name, student.last_name + " energy has increased!\x1b[0m\n" +
              "Actual energy level is", student.energy_level, "\n")
        time.sleep(2)

    def do_coding_dojo(self, student1, student2):
        """
        Executes mentor's coding dojo program in order to increase student knowledge.

        Args:
            student1: Student object
            student2: Student object
        Returns:
            None
        """
        print("\n\033[1mMentor " + self.first_name + " does Coding Dojo for ", student1.first_name, student1.last_name,
              "and", student2.first_name, student2.last_name + "\033[0m\n")
        time.sleep(2)
        self.humanity_level += 1
        student1.energy_level -= 2
        student2.energy_level -= 3
        student1.knowledge_level += 2
        student2.knowledge_level -= 1
        print("\x1b[31mMentors humanity has decreased!!!\x1b[0m\n" + self.first_name, self.last_name +
              " has " + str(self.humanity_level) + " humanity points now.")
        time.sleep(0.5)
        print("\x1b[32mStudent " + student1.first_name, student1.last_name + " energy has increased!\x1b[0m\n" +
              "Actual energy level is", student1.energy_level, "\n")
        time.sleep(0.5)
        print("\x1b[31mStudent " + student2.first_name, student2.last_name + " energy has decreased!\x1b[0m\n" +
              "Actual energy level is", student2.energy_level, "\n")
        time.sleep(0.5)
        print("\x1b[32mStudent " + student1.first_name, student1.last_name +
              " know much more now. \x1b[0m\n" +
              "Actual knowledge level is", student1.knowledge_level, "\n")
        time.sleep(0.5)
        print("\x1b[31mStudent " + student2.first_name, student2.last_name +
              " doesn't understand to much.\x1b[0m\n" +
              "Actual knowledge level is", student2.knowledge_level, "\n")
        time.sleep(3)

    def say_joke(self, student):
        """
        Executes mentor's program to say a joke in order to increase student energy.

        Args:
            student: Student object
        Returns:
            None
        """

        print("\n\033[1mMentor " + self.first_name + " says joke to ", student.first_name, student.last_name + "\033[0m\n")
        choose_joke = random.randint(0, 2)
        if choose_joke == 0:
            print("""
                    Why do Java programmers have to wear glasses?
                    """)
            time.sleep(3)
            print("""
                    Because they don't C#
                    \n""")
            time.sleep(3)
            self.humanity_level += 1
            student.energy_level -= 2
            print("\x1b[32mMentors humanity has increased.\x1b[0m\n" + self.first_name,
                  self.last_name + " has " + str(self.humanity_level) + " humanity points now.")
            time.sleep(0.5)
            print("\x1b[31mStudent " + student.first_name, student.last_name + " energy has decreased!\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(0.5)
            print("\x1b[33mStudent " + student.first_name, student.last_name +
                  " knowledge level is the same... o_O\x1b[0m\n" +
                  "Actual knowledge level is", student.energy_level, "\n")
            time.sleep(3)
        elif choose_joke == 1:
            print("""
                    What would be if women have programmed nuclear power plants?
                    """)
            time.sleep(3)
            print("""
                    Nothing would be!
                    \n""")
            time.sleep(3)
            self.humanity_level += 2
            student.energy_level += 2
            print("\x1b[32mMentors humanity has increased.\x1b[0m\n" + self.first_name,
                  self.last_name + " has " + str(self.humanity_level) + " humanity points now.")
            time.sleep(0.5)
            print("\x1b[31mStudent " + student.first_name, student.last_name + " energy has decreased!\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(0.5)
            print("\x1b[33mStudent " + student.first_name, student.last_name +
                  " knowledge level is the same... o_O\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(3)
        else:
            print("""
                    What's the object-oriented way to become wealthy?
                    """)
            time.sleep(3)
            print("""
                    Inheritance.\n
                    """)
            time.sleep(3)
            self.humanity_level += 3
            student.energy_level += 3
            print("\x1b[32mMentors humanity has increased.\x1b[0m\n" + self.first_name,
                  self.last_name + " has " + str(self.humanity_level) + " humanity points now.")
            time.sleep(0.5)
            print("\x1b[31mStudent " + student.first_name, student.last_name + " energy has decreased!\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(0.5)
            print("\x1b[33mStudent " + student.first_name, student.last_name +
                  " knowledge level is the same... o_O\x1b[0m\n" +
                  "Actual energy level is", student.energy_level, "\n")
            time.sleep(3)

import re

import bs4
import requests


class Problem:
    """Class for objects that contain information about a Problem

    Attributes
    ----------
    link : str
        Link to the Problem at codeforces.com
    soup : bs4.BeautifulSoup
        HTML data of the problem
    input : list[SampleTest]
        List of strings containing the input specification
    is_testcased : bool
        Indicates whether the problem has testcases (t)
    tests : list[Problem.SampleTest]
        List of Problem.SampleTest objects

    Methods
    -------
    mark_latex_symbols(line) -> str
        Marks all latex symbols individually
    get_sample_tests(soup) -> list[Problem.SampleTest]
        Returns a list of Problem.SampleTest objects
    """

    def __init__(self, contestId, index):
        self.link = f"https://codeforces.com/contest/{contestId}/problem/{index}"
        self.soup = bs4.BeautifulSoup(
            requests.get(
                self.link,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.61 Chrome/126.0.6478.61 Not/A)Brand/8  Safari/537.36"
                },
            ).text,
            "html.parser",
        )
        self.input = [
            self.mark_latex_symbols(line)
            for line in self.soup.find("div", "input-specification").stripped_strings
        ]
        self.is_testcased = True
        self.tests = self.get_sample_tests(self.soup)

    def mark_latex_symbols(self, line):
        pattern = r"\$\$\$[^$]*\$\$\$"
        expressions = re.findall(pattern, line)
        for expression in expressions:
            new_match = " ".join(["$" + x + "$" for x in expression[3:-3].split()])
            line = line.replace(expression, new_match)
        return line

    def get_sample_tests(self, soup):
        tc_soup = soup.find("div", "sample-test")
        inputs = tc_soup.find_all("div", "input")
        outputs = tc_soup.find_all("div", "output")
        return [
            Problem.SampleTest(input, output, self)
            for input, output in zip(inputs, outputs)
        ]

    def __repr__(self):
        return f"Input:\n{self.input}\n\nTests:\n{self.tests}"

    class SampleTest:
        """Class for objects that represent a sample test

        Attributes
        ----------
        T : int
            Number of testcases
        input : bs4.element.Tag
        output : bs4.element.Tag

        Methods
        -------
        get_no_of_testcases(soup, problem) -> int
            Returns the number of testcases in the sample test
        """

        def __init__(self, input, output, problem):
            self.T = self.get_no_of_testcases(input, problem)
            self.input = "\n".join(input.stripped_strings)
            self.output = "\n".join(output.stripped_strings)

        def get_no_of_testcases(self, soup, problem):
            try:
                # finds the last testcase so as to get the number of testcases
                last_testcase = str(soup.find_all("div", "test-example-line")[-1])
                match = re.search(r"test-example-line-(\d)", last_testcase)
                T = int(match.group(1))

                if T >= 1:
                    return T
                else:
                    problem.is_testcased = False
                    return 1
            except ValueError:
                problem.is_testcased = False
                return 1

        def __repr__(self):
            return f"T: {self.T}\n\n{self.input}\n\n{self.output}"

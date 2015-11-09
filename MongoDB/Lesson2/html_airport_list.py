#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []

    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        airports = soup.find(id="AirportList")
        lines = airports.find_all("option")
        for code in lines:
            item = code.get("value")
            if 'All' not in item:
                data.append(code.get("value"))

    print len(data)
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
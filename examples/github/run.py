# -*- coding: utf-8 -*-
from grab.spider import Spider, Task


class GithubSpider(Spider):
    start_url = 'https://github.com/explore'

    def task_generator(self):
        yield Task('start', url=self.start_url)

    def task_start(self, grab, task):
        print("Start: {}".format(grab.doc.url))
        explore_grid_hrefs = grab.doc(
            '//a[contains(@class, "exploregrid-item")]').attr_list('href')
        for href in explore_grid_hrefs:
            url = grab.make_url_absolute(href)
            yield Task('explore', url=url)

    def task_explore(self, grab, task):
        print('Explore: {}'.format(grab.doc.url))
        repos_hrefs = grab.doc('//h3[@class="mb-1"]/a').attr_list('href')
        for href in repos_hrefs:
            url = grab.make_url_absolute(href)
            yield Task('repo', url=url)

    def task_repo(self, grab, task):
        print('Repo: {}'.format(grab.doc.url))
        commits_number = grab.doc('//li[@class="commits"]/a/span').text()
        print("{} commits number: {}".format(grab.doc.url, commits_number))


if __name__ == '__main__':
    bot = GithubSpider(http_api_port=8888)
    bot.run()

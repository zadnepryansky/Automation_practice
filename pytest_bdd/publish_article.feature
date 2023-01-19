

Feature: Blog
  A site where you can .

  Scenario Outline: Go to the page
    Given Our driver
    And Customized URL '<url>'

    When I navigate to the page

    Then Werify the page content

    Examples:
      | url                   |
      | https://wikipedia.org |
      | https://aqa.science   |
      | https://google.com    |
      | https://adv.wiki      |
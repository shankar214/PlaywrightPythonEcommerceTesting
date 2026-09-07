Feature: order transaction
           Tests related to order Trasactions

Scenario Outline:verify Order success message show in details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When I Login to portal with <username> and <password>
    And navigate to the orders page
    And select the orderId
    Then order message is succesfully displayed 
    Examples:
      | username         | password |
      |shiva125@gmail.com|21it6051@R |

## **PERF-0003:** Performance testing - POS 1000 checkouts  

> **Summary:** Verify that the app can perform 1000 checkouts successively.  <br>

**Preconditions:**
 - Products and inventory must not be empty, enough for 1000 transactions.  
 - All transactions had been cleared or is empty.  

Scenario 1 

 | \# | Step | Expected Behavior | 
 |----|------|-------------------| 
 |  1 | Launch application.                    | Verify that the `Checkout` screen is displayed. | 
 |  2 | Tap the first item in the inventory.   | Verify that the default quantity is "1". | 
 |  3 | Tap the `Add to Cart` button.          | Verify that the item count increments by "1". | 
 |  4 | Tap the `Go to Cart` button.           | Verify that the total item count is "1". | 
 |  5 | Tap the `Checkout` button.             | Verify that `Cash` option is highlighted.  | 
 |  6 | Tap the `Next` button.                 | Verify that the `Cash Payment` screen is displayed. | 
 |  7 | Tap the `Charge` button.               | Verify the `Done` screen is shown. | 
 |  8 | Tap the `New Sale` button.             | Verify the `Checkout` screen  is shown. | 
 |  9 | Repeat scenario 999 times.             | Verify that all transactions are successful. |  
 | 10 | In the appbar, tap the hamburger icon. | Verify that the sidebar menu is opened. |   
 | 11 | In the sidebar, tap `Transactions` menu item. | Verify that the `Transactions` screen is shown. |   
 | 12 | Check the number of daily sales. | Verify that the daily sales is "1000". |    

**Post-conditions:**  

 - All the 1000 sales are recorded.

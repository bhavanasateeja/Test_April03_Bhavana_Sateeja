from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

'''
Bhavana Sateeja - to update an order, first we need to create an order to change the status from available to pending and get the order_id 
Then use patch to update the status from pending to sold and lastly using get for pet id, validate the status is sold
'''
def test_patch_order_by_id():
    test_endpoint = "/store/order"
    response = api_helpers.post_api_data(test_endpoint, {"pet_id": 2})
    order_id = response.json()["id"]
    print(order_id)

    test_endpoint_patch = f"/store/order/{order_id}"
    response_patch = api_helpers.patch_api_data(test_endpoint_patch, {"status": "sold"})
    # print(response_patch.status_code)
    # print(response_patch.json()["message"])
    assert response_patch.status_code == 200, "status code is not 200"
    assert response_patch.json()["message"] == "Order and pet status updated successfully", "Order is not being updated successfully"

    test_endpoint_get_status_by_pet_id = "/pets/2"
    response_get_status_by_pet_id = api_helpers.get_api_data(test_endpoint_get_status_by_pet_id)
    print(response_get_status_by_pet_id)
    # print(response_get_status_by_pet_id.json()["status"])
    assert response_get_status_by_pet_id.json()["status"] == "sold", "status is not correct after update"


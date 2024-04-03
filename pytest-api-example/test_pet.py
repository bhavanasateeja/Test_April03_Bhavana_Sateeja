from jsonschema import validate
import pytest
import schemas
import api_helpers
from app import PET_STATUS
from hamcrest import assert_that, contains_string, is_
from jsonschema.exceptions import ValidationError

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)
    # print(response)
    # print(response.json())
    # print(schemas.pet)

    assert response.status_code == 200

    '''  Bhavana Sateeja - manually validated the returned schema with actual schema using https://www.jsonschemavalidator.net/ 
    and found out that for name we are expecting integer and got string
    Changed type to string for name in schemas.py (as part of test_find_by_status_200) as it was incorrect
    '''
    # json_2 = {'id': 1, 'name': 1, 'type': 'dog', 'status': 'pending'}
    # validate(json_2, schema=schemas.pet)

    '''Bhavana Sateeja - Validate the response schema against the defined schema in schemas.py
    Since the returned scheme is not correct, exception should be caught and assertion need to be added.
    '''
    try:
        validate(instance=response.json(), schema=schemas.pet)
    except Exception as err:
        # jsonschema.exceptions.ValidationError: 'ranger' is not of type 'integer'
        # print(err)
        print("Returned schema is not a valid schema as per schema.py")
        assert False, "Returned schema is not a valid schema as per schema.py"

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
'''
Bhavana Sateeja - Found PET_STATUS list with all statuses in app.py
'''
@pytest.mark.parametrize("status", PET_STATUS)
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200, 'response code is not 200'
    '''
    Bhavana Sateeja - need to validate the status for each response. Ex. pet type cat and fish are available, dog is pending and no result for sold
    '''
    print(response.json())
    for i in response.json():
        assert i['status'] == status, "status is incorrect"
        validate(i, schema=schemas.pet)

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
@pytest.mark.parametrize("pet_id", range(5, 10))
def test_get_by_id_404(pet_id):
# def test_get_by_id_404(pet_id=9):
    # TODO...
    '''Bhavana Sateeja - got the endpoint from Swagger page and added steps to get response and validate response code
    Parametrizing it by giving list range(5, 10) for id's that does not exist
    '''
    test_endpoint = "/pets/{pet_id}"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 404, 'response code is not 404'


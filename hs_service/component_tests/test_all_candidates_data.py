def test_get_all_candidates_returns_200_status_code(hs_test_helper):
    """
    1. Calls get to all candidates endpoint
    2. Expects status code 200
    """
    r = hs_test_helper.get_all_candidates()
    assert r.status_code == 200, f"failed to get expected status_code expected 200, instead got: {r.status_code}"


def test_get_all_candidates_returns_expected_payload(hs_test_helper, hs_data_factory):
    """
    1. Calls GET to all candidates endpoint
    2. Asserts response payload to be as expected
    """
    expected_payload = hs_data_factory.exp_resp_data_payload()
    r = hs_test_helper.get_all_candidates()
    assert r.json() == expected_payload, \
        f"failed to get expected payload, expected: {expected_payload}, instead got: {r.text}"


def test_get_all_candidates_returns_the_expected_candidates_by_their_emails(hs_test_helper, hs_data_factory):
    """
    1. Calls GET to all candidates endpoint
    2. Asserts response payload contains the expected candidates by their email addresses
    """
    expected_candidates_emails = sorted(hs_data_factory._EXP_CANDIDATES_EMAIL_ADDRESSES)
    r = hs_test_helper.get_all_candidates()
    actual_candidates_emails = sorted([i['contact_info']['email'] for i in r.json()])
    assert actual_candidates_emails == expected_candidates_emails, \
        f"failed to get expected candidates emails, expected: {expected_candidates_emails}, " \
        f"instead got: {actual_candidates_emails}"

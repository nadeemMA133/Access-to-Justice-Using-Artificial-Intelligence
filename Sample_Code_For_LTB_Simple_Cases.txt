import requests

def analyze_case(url):
    """
    Reads text from an HTTPS source, checks legal keywords,
    evaluates rent payment status, and produces a decision.
    """

    # ---- 1. Read content from URL ----
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        text = response.text.lower()
    except Exception as e:
        return f"Error reading URL: {e}"

    # ---- 2. Look for keywords ----
    keywords = ["landlord", "tenant", "ltb"]
    found_keywords = [k for k in keywords if k in text]

    # ---- 3. Look for rent payment status ----
    rent_paid = None

    if "rent_paid_last_60_days: yes" in text:
        rent_paid = True
    elif "rent_paid_last_60_days: no" in text:
        rent_paid = False

    # ---- 4. Produce a decision ----
    if rent_paid is False:
        decision = (
            "Decision: The tenant must vacate the property due to non-payment "
            "of rent within the last 60 days, in accordance with LTB rules."
        )
    elif rent_paid is True:
        decision = (
            "Decision: Rent has been paid within the last 60 days. "
            "Eviction based on non-payment is not applicable."
        )
    else:
        decision = (
            "Decision: Unable to determine rent payment status because the text "
            "does not indicate 'rent_paid_last_60_days: yes/no'."
        )

    # ---- 5. Build result ----
    result = {
        "keywords_found": found_keywords,
        "rent_paid_last_60_days": rent_paid,
        "decision": decision
    }

    return result

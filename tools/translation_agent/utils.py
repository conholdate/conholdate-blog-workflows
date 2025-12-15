import requests
import time
import uuid
from datetime import datetime, timedelta, timezone
import config


def send_metrics(run_id, 
                 status, 
                 run_duration_ms, 
                 agent_name,
                 job_type,
                 item_name, 
                 items_discovered,
                 items_failed,
                 items_succeeded, 
                 website,
                 website_section    = config.WEBSITE_SECTION_BLOG,
                 agent_owner        = config.AGENT_OWNER, 
                 product            = config.JOB_ALL_PRODUCTS, 
                 platform           = config.JOB_ALL_PLATFORMS
                 ):
    payload = {
        "timestamp"         : datetime.now(timezone(timedelta(hours=5))).isoformat(),
        "agent_name"        : agent_name,
        "agent_owner"       : agent_owner,
        "job_type"          : job_type,
        "run_id"            : run_id,
        "status"            : status,
        "product"           : product,
        "platform"          : platform,
        "website"           : website,
        "website_section"   : website_section,
        "item_name"         : item_name,
        "items_discovered"  : items_discovered,
        "items_failed"      : items_failed,
        "items_succeeded"   : items_succeeded,
        "run_duration_ms"   : run_duration_ms
    }
    print(f"PAYLOAD:\n{payload}")
    
    if config.PRODUCTION_ENV:
        try:
            response = requests.post(f"{config.METRICS_URL}?token={config.METRICS_TOKEN}", json=payload, headers={"Content-Type": "application/json"})
            if response.status_code == 200:
                print("✅ Metrics sent successfully")
            else:
                print(f"Failed to send metrics: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Error sending metrics: {e}")

    try:
        payload["run_env"] = "PROD" if config.PRODUCTION_ENV else "DEV"
        print(f"PAYLOAD:\n{payload}")
        response = requests.post(f"{config.METRICS_URL_DEV}?token={config.METRICS_TOKEN_DEV}", json=payload, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            print("✅ Metrics sent successfully")
        else:
            print(f"Failed to send metrics: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error sending metrics: {e}")
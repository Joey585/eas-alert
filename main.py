"""
ORG — Originator code; programmed per unit when put into operation[8]

PEP – National Public Warning System (Previously known as "Primary Entry Point System". It will be FEMA for National Tests through the Legacy format instead of IPAWS.)
President or other authorized national officials
CIV – Civil authorities
i.e. Governor, state/local emergency management, local police/fire officials
WXR – National Weather Service (or Environment Canada.)
Any weather-related alert
EAS – EAS Participant (or Broadcast station or cable system)
Broadcasters. Generally only used with test messages.
EAN – Emergency Action Notification Network (No longer used after ~2010.)
Used to send Emergency Action Notifications. (No longer used, replaced by PEP.)

EEE — Event code; programmed at time of event

PSSCCC — Location codes (up to 31 location codes per message), each beginning with a dash character; programmed at time of event

In the United States, the first digit (P) is zero if the entire county or area is included in the warning, otherwise, it is a non-zero number depending on the cardinal location of the emergency within the area.[9] The remaining five digits are the FIPS state (SS) and county code (CCC). The entire state may be specified by using county code 000 (three zeros).
In Canada, all six digits make up a Canadian Location Code, which corresponds to a specific forecast region as used by the Meteorological Service of Canada. All forecast region numbers are six digits with the first digit always zero.
5. TTTT — Purge time of the alert event (from exact time of issue)

In the format hhmm, using 15-minute increments up to one hour, using 30-minute increments up to six hours, and using hourly increments beyond six hours. Weekly and monthly tests sometimes have a 12-hour or greater purge time to assure users have an ample opportunity to verify reception of the test event messages; however; 15 minutes is more common, especially on NOAA Weather Radio's tests.
For short term events (like a tornado) this value could be set to 0000 (four zeros), which will purge the warning immediately after the message has been received. However, this is not typical, and FCC guidelines suggest a minimum of 15 minutes purge time.
The purge time is not intended to coincide with the actual end of the event. Longer events that may not end for days (like hurricanes) may have a purge time of only a few hours. That an event message has been purged does not indicate or imply that the threat has passed.
The National Weather Service is changing the maximum purge time for alerts on NOAA Weather Radio from 6 hours to 99.5 hours by summer 2023 to address long duration events purging before the event begins. [10]

JJJHHMM — Exact time of issue, in UTC, (without time zone adjustments).

JJJ is the Ordinal date (day) of the year, with leading zeros
HHMM is the hours and minutes (24-hour format), in UTC, with leading zeros
LLLLLLLL — Eight-character station callsign identification, with "/" used instead of "–" (such as the first eight letters of a cable headend's location, WABC/FM for WABC-FM, KLOX/NWS for a weather radio station programmed from Los Angeles, or EC/GC/CA for a Weatheradio Canada station).

Each field of the header code is terminated by a dash character, including the station ID at the end; individual PSSCCC location numbers are also separated by dashes, with a plus (+) separating the last location from the purge time that follows it.
"""
from create_eas import create_eas

create_eas(
    "PEP",
    "CEM",
    ["13075", "06033"],
           "This is an Primary Entry Point Alert issued by the President of the United States. The Trump Dead Squad has been deployed and is now heading to the following counties of Illinois: Cook, and Lake. Please accept your fate as the squads closes in on the woke mind virus.",
    "1200",
    "3290422",
    "WBBM/FM",
    "eas.wav"
           )

import predictionio
from datetime import datetime
import pytz

# Create a FileExporter and specify "my_events.json" as destination file
exporter = predictionio.FileExporter(file_name="my_events.json")

event_properties = {
    "someProperty" : "value1",
    "anotherProperty" : "value2",
    }
# write the events to a file
event_response = exporter.create_event(
    event="my_event",
    entity_type="user",
    entity_id="uid",
    target_entity_type="item",
    target_entity_id="iid",
    properties=event_properties,
    event_time=datetime(2014, 12, 13, 21, 38, 45, 618000, pytz.utc))

# ...

# close the FileExporter when finish writing all events
exporter.close()
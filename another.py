def handler(event,context):
    for i in range(1000,1099):
      print(i)
    print event
    return event['data']

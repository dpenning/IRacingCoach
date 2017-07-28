# IRacingCoach
a collection of tools being used to improve myself at IRacing

Server implementation
======

- background process that should be running at all times
  - handle the connection to the iracing sdk
    - js iracing sdk - https://www.npmjs.com/package/node-irsdk
  - logging component that saves to files

- webserver
  - serve a regular page that loads data for UI
    - standard frameworks for serving web pages.
    react/redux
  - websockets implementation that also reads from iracing sdk and sends data up to client to parse
    - smoothie charts for realtime charts - http://smoothiecharts.org/
    - highcharts for lap analysis - https://www.highcharts.com/

  

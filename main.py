import variables
import backtestdata

symbols = variables.symbols
timeframe = variables.timeframe
from_datetime = variables.from_datetime
till_datetime = variables.till_datetime
cex = variables.cex
time_frames = variables.time_frames
#limit = variables.limit
initialInvestment = variables.initialInvestment
time_offset = time_frames[timeframe]

df = backtestdata.getalldata(symbols, timeframe, from_datetime, till_datetime, cex, time_offset)
from hamutils import LogFile
x=LogFile()
logfile="BarcodeScan_091699b3e9224e128a46e5afe00eac9d_Trace.trc"
trc=x.open(logfile)
# for line in trc.readlines():
#     print(line)
    # pass
for item in trc.find('Clean'):
    print(item)


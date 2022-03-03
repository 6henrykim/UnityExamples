from pysensationcore import *
import sensation_helpers as sh

prefix = "point"
polylinePath = createInstance("PolylinePath", "PolylinePathInstance")
points = sh.createList(6)
connect(points["output"], polylinePath.points)

fingerPatch = sh.createSensationFromPath("Star",
                        {
                            ("middleFinger_intermediate_position", points["inputs"][0]) : (-0.04998946,0.1598181,0.05967208),
                            ("thumb_metacarpal_position", points["inputs"][1]) : (-0.00795498,0.1333526,-0.05546868),
                            ("pinkyFinger_proximal_position", points["inputs"][2]) : (-0.08053764,0.1449668,0.005471267),
                            ("indexFinger_proximal_position", points["inputs"][3]) : (-0.02041978,0.1583857,0.03082177),
                            ("wrist_position", points["inputs"][4]) : (-0.03404539,0.1322506,-0.0783692),
                            ("middleFinger_intermediate_position", points["inputs"][5]) : (-0.04998946,0.1598181,0.05967208)
                        },
                        output = polylinePath.out,
                        drawFrequency = 101,
                        definedInVirtualSpace = True,
                        renderMode = sh.RenderMode.Bounce
                        )
                        
setMetaData(fingerPatch.middleFinger_intermediate_position, "Input-Visibility", False)                        
setMetaData(fingerPatch.thumb_metacarpal_position, "Input-Visibility", False)
setMetaData(fingerPatch.pinkyFinger_proximal_position, "Input-Visibility", False)
setMetaData(fingerPatch.indexFinger_proximal_position, "Input-Visibility", False)
setMetaData(fingerPatch.wrist_position, "Input-Visibility", False)
setMetaData(fingerPatch.middleFinger_intermediate_position, "Input-Visibility", False)
                        
import traci
import time

class Run_SUMO:
    def __init__(self, type1, type2):
        self.type1 = type1
        self.type2 = type2

    def _process_red_detector(self, detector_id):
        vehicles = traci.inductionloop.getLastStepVehicleIDs(detector_id)
        for vehicle_id in vehicles:
            current_lane = traci.vehicle.getLaneID(vehicle_id)
            adjacent_lanes = traci.lane.getLinks(current_lane)
            if adjacent_lanes:
                new_lane = int(adjacent_lanes[0][0].split("_")[-1])
                traci.vehicle.changeLane(vehicle_id, new_lane, 0)

    def _process_blue_detector(self, detector_id):
        vehicles = traci.inductionloop.getLastStepVehicleIDs(detector_id)
        # print(f"Vehicles detected: {vehicles}")

        for vehicle_id in vehicles:
            try:
                if traci.vehicle.getTypeID(vehicle_id) == self.type1:
                    traci.vehicle.setType(vehicle_id, self.type2)
            except:
                print(f"Vehicles {vehicle_id} is no longer in the street.")


    def run(self, config,
            red_detectors:list, 
            blue_detectors:list):
        
        traci.start(["sumo", "-c", config, "--start"])
        time.sleep(3)
        step = 0

        while step < 3620:
            traci.simulationStep()
            
            for detector in red_detectors:
                self._process_red_detector(detector)
            for detector in blue_detectors:
                self._process_blue_detector(detector)
            
            step += 1

        traci.close()

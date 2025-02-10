import analyzers
import dchar
import batcaphis
import tech_spec
import battery_activity
import userdetails

def test_worker_nodes():
    userdetails.get_details()
    analyzers.analyse()
    tech_spec.tech_specification()
    dchar.dcharecter()
    dchar.generate_graph()
    batcaphis.capacity()
    battery_activity.activity()

if __name__ == "__main__":
    test_worker_nodes()

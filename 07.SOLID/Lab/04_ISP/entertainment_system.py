class EntertainmentDevice:
    pass


class HDMIConnectableMixin:
    def connect_to_device_via_hdmi_cable(self, device):
        return f"Connected {self} to {device} with HDMI cable"


class EthernetConnectableMixin:
    def connect_to_device_via_ethernet_cable(self, device):
        return f"Connected {self} to {device} with Ethernet cable"


class RCAConnectableMixin:
    def connect_to_device_via_rca_cable(self, device):
        return f"Connected {self} to {device} with RCA cable"


class PowerOutletConnectableMixin:
    def connect_device_to_power_outlet(self):
        return f"{self} connected to power outlet"


class Television(EntertainmentDevice, RCAConnectableMixin, HDMIConnectableMixin,
                 PowerOutletConnectableMixin):
    def connect_to_dvd(self, dvd_player):
        return self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet()


class DVDPlayer(EntertainmentDevice, HDMIConnectableMixin, PowerOutletConnectableMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet()


class GameConsole(EntertainmentDevice, HDMIConnectableMixin, EthernetConnectableMixin,
                  PowerOutletConnectableMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class Router(EntertainmentDevice, EthernetConnectableMixin, PowerOutletConnectableMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


ps5 = GameConsole()
tv = Television()
print(tv.connect_device_to_power_outlet())
print(tv.connect_to_device_via_hdmi_cable(ps5))

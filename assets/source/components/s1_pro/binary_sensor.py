import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_UART_ID
from esphome.components import binary_sensor, uart

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["binary_sensor", "number"]

ns = cg.esphome_ns.namespace("s1_pro")
LD2450 = ns.class_("LD2450", cg.Component, uart.UARTDevice)
CONF_BLUETOOTH_STATE = "bluetooth_state"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(LD2450),
    cv.Required(CONF_UART_ID): cv.use_id(uart.UARTComponent),
    cv.Optional(CONF_BLUETOOTH_STATE): binary_sensor.binary_sensor_schema(),

}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_BLUETOOTH_STATE in config:
        bt_state = await binary_sensor.new_binary_sensor(config[CONF_BLUETOOTH_STATE])
        cg.add(var.set_bluetooth_state_sensor(bt_state))

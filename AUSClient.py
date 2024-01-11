from __future__ import annotations
import os
import sys
import asyncio
import typing
import bsdiff4
import shutil

import Utils

from NetUtils import NetworkItem, ClientStatus
from worlds import aus
from MultiServer import mark_raw
from CommonClient import CommonContext, server_loop, \
    gui_enabled, ClientCommandProcessor, logger, get_base_parser
from Utils import async_start


class AUSCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

class AUSContext(CommonContext):
    tags = {"AP", "Online"}
    game = "AUS"
    command_processor = AUSCommandProcessor
    items_handling = 0b111

    def __init__(self, server_address, password):
        super().__init__(server_address, password)

    # def clear_AUS_files(self):
        # path = self.save_game_folder
        # self.finished_game = False
        # for root, dirs, files in os.walk(path):
        #     for file in files:
        #         if "check.spot" == file or "scout" == file:
        #             os.remove(os.path.join(root, file))
        #         elif file.endswith((".item", ".victory", ".route", ".playerspot", ".mad", 
        #                                     ".youDied", ".LV", ".mine", ".flag", ".hint")):
        #             os.remove(os.path.join(root, file))

    async def connect(self, address: typing.Optional[str] = None):
        # self.clear_AUS_files()
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        # self.clear_AUS_files()
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        # self.clear_AUS_files()
        await super().connection_closed()

    async def shutdown(self):
        # self.clear_AUS_files()
        await super().shutdown()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game
        async_start(process_AUS_cmd(self, cmd, args))

async def process_AUS_cmd(ctx: AUSContext, cmd: str, args: dict):
    if cmd == "Connected":
        filename = f"check.spot"
        # with open(os.path.join(ctx.save_game_folder, filename), "a") as f:
        #     for ss in set(args["checked_locations"]):
        #         f.write(str(ss-12000)+"\n")
        #     f.close()
    elif cmd == "LocationInfo":
        for l in args["locations"]:
            locationid = l.location
        #     filename = f"{str(locationid-12000)}.hint"
        #     with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
        #         toDraw = ""
        #         for i in range(20):
        #             if i < len(str(ctx.item_names[l.item])):
        #                 toDraw += str(ctx.item_names[l.item])[i]
        #             else:
        #                 break
        #         f.write(toDraw)
        #         f.close()
    elif cmd == "Retrieved":
        print('dummmy function')
    elif cmd == "SetReply":
        print('setreply')
    elif cmd == "ReceivedItems":
        print('ReceivedItems')
    elif cmd == "RoomUpdate":
        print('RoomUpdate')

    elif cmd == "Bounced":
        print('Bounced')
        # tags = args.get("tags", [])
        # if "Online" in tags:
        #     data = args.get("data", {})
        #     if data["player"] != ctx.slot and data["player"] is not None:
        #         filename = f"FRISK" + str(data["player"]) + ".playerspot"
        #         with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
        #             f.write(str(data["x"]) + str(data["y"]) + str(data["room"]) + str(
        #                 data["spr"]) + str(data["frm"]))
        #             f.close()

async def game_watcher(ctx: AUSContext):
    while not ctx.exit_event.is_set():
        path = ctx.save_game_folder
        sending = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if "DontBeMad.mad" in file:
                    os.remove(os.path.join(root, file))
        await asyncio.sleep(0.1)


def main():
    Utils.init_logging("AUSClient", exception_logger="Client")

    async def _main():
        ctx = AUSContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        asyncio.create_task(
            game_watcher(ctx), name="AUSProgressionWatcher")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="AUS Client, for text interfacing.")
    args = parser.parse_args()
    main()

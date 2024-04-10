/** @odoo-module **/

// /** ********************************************************************************
//     Copyright 2020 Creu Blanca
//     Copyright 2017-2019 MuK IT GmbH
//     License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
//  **********************************************************************************/

import {registry} from "@web/core/registry";
import {patch} from "@web/core/utils/patch";
import {listView} from "@web/views/list/list_view";
import {FileListRenderer} from "./file_list_renderer.esm";
// import {FileListController} from "./file_list_controller.esm";
import {ListController} from "@web/views/list/list_controller";

import {createFileDropZoneExtension, createFileUploadExtension} from "./dms_file_upload.esm";

patch(FileListRenderer.prototype, createFileDropZoneExtension());
patch(ListController.prototype, createFileUploadExtension());
FileListRenderer.template = "dms.ListRenderer";

export const FileListView = {
    ...listView,
    buttonTemplate: "dms.ListButtons",
    Renderer: FileListRenderer,
};

registry.category("views").add("file_list", FileListView);

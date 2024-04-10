/** @odoo-module **/

// /** ********************************************************************************
//     Copyright 2020 Creu Blanca
//     Copyright 2017-2019 MuK IT GmbH
//     License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
//  **********************************************************************************/

import {registry} from "@web/core/registry";
import {patch} from "@web/core/utils/patch";
import {kanbanView} from "@web/views/kanban/kanban_view";
import {FileKanbanRenderer} from "./file_kanban_renderer.esm";
// import {FileKanbanController} from "./file_kanban_controller.esm";
import {KanbanController} from "@web/views/kanban/kanban_controller";

import {createFileDropZoneExtension, createFileUploadExtension} from "./dms_file_upload.esm";

patch(FileKanbanRenderer.prototype, createFileDropZoneExtension());
patch(KanbanController.prototype, createFileUploadExtension());
FileKanbanRenderer.template = "dms.KanbanRenderer";

export const FileKanbanView = {
    ...kanbanView,
    buttonTemplate: "dms.KanbanButtons",
    Renderer: FileKanbanRenderer,
};

registry.category("views").add("file_kanban", FileKanbanView);

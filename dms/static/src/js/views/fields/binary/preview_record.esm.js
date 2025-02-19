/** @odoo-module **/

import {registry} from "@web/core/registry";
import {BinaryField} from "@web/views/fields/binary/binary_field";
import {useService} from "@web/core/utils/hooks";

export class PreviewRecordField extends BinaryField {
    setup() {
        super.setup();
        this.messaging = useService("mail.messaging");
        this.dialog = useService("dialog");
    }

    onFilePreview() {
        const self = this;
        this.messaging.get().then((messaging) => {
            const attachmentList = messaging.models.AttachmentList.insert({
                selectedAttachment: messaging.models.Attachment.insert({
                    id: self.props.record.resId,
                    filename: self.props.record.data.display_name || "",
                    name: self.props.record.data.display_name || "",
                    mimetype: self.props.record.data.mimetype,
                    model_name: self.props.record.resModel,
                }),
            });
            this.dialog = messaging.models.Dialog.insert({
                attachmentListOwnerAsAttachmentView: attachmentList,
            });
        });
    }
}

PreviewRecordField.template = "dms.FilePreviewField";

const previewRecordField = {
    component: PreviewRecordField,
    dependencies: [BinaryField],
    display_name: "Preview Record",
    supportedTypes: ["binary"],
}
registry.category("fields").add("preview_binary", previewRecordField);

/** @odoo-module **/

import {registry} from "@web/core/registry";
import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {Component, onWillUpdateProps} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";

class DmsPathField extends Component {
    static template = "dms.DmsPathField";
    static props = {
        ...standardFieldProps,
    };

    setup() {
        super.setup();
        this.action = useService("action");
        this.formatData(this.props);
        onWillUpdateProps((nextProps) => this.formatData(nextProps));
    }

    formatData(props) {
        this.data = JSON.parse(props.record.data?.path_json || "[]");
    }

    _onNodeClicked(event) {
        event.preventDefault();
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: $(event.currentTarget).data("model"),
            res_id: $(event.currentTarget).data("id"),
            views: [[false, "form"]],
            target: "current",
            context: {},
        });
    }
}

const dmsPathField = {
    component: DmsPathField,
    display_name: "Dms Path Field",
    supportedTypes: ["text"],
    extractProps: () => {
        return {};
    },
};

registry.category("fields").add("path_json", dmsPathField);

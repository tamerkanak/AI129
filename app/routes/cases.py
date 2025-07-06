from flask import Blueprint, render_template
from flask_login import login_required
from ..models import Case

cases_bp = Blueprint('cases', __name__)

@cases_bp.route('/case/<int:case_id>')
@login_required
def case_detail(case_id):
    case = Case.query.get_or_404(case_id)
    return render_template('case_detail.html', case=case) 